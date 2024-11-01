pragma solidity ^0.8.0;

contract VulnerableContract {
    address payable public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    // Reentrancy vulnerability
    function withdraw(uint _amount) public {
        require(msg.sender == owner, "Only owner can withdraw");
        require(address(this).balance >= _amount, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");
    }

    // Integer overflow/underflow vulnerability
    function addFunds(uint _amount) public {
        uint newBalance = address(this).balance + _amount;
        require(newBalance >= address(this).balance, "Overflow");
        // Add funds (insecure handling)
    }

    // Unchecked call
    function transferTo(address payable _to) public payable {
        _to.call{value: msg.value}("");
    }

    // Use of tx.origin
    function isOwner() public view returns (bool) {
        return tx.origin == owner;
    }
}
