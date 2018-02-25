pragma solidity 0.4.20;

contract getSchwifty {
  string internal constant seeWhatYouGot = "I want to see what you got!";
  string internal contestResult;
  
  // Contract constructor that takes a string param
  function getSchwifty(string _contestResult) public {
    contestResult = _contestResult;
  }
  
  function showMeWhatYouGot() external pure returns (string) {
    return seeWhatYouGot;  
  }
  
  function enterContest(string _contestEntry) external view returns (string) {
    // completely disregard the _contestEntry ;)
    return contestResult;
  }
} 
