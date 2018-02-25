contract startup{  
  mapping (address => uint) balances;

  address public settlor;
  address public beneficiary;
  address public court;
  address public protector;
  address public startup = msg.sender;
  bool settlorApprove;
  bool courtApprove;

  function setup(address settlor, address beneficiary, address protector, address court){
    if(msg.sender == startup){
        settlor = settlor;
        beneficiary = beneficiary;
	protector = protector;
	court = court;
    }
  }

  function approve(){
    if(msg.sender == settlor) settlorApprove = true;
    else if(msg.sender == court) courtApprove = true;
    if(settlorApprove || courtApprove) fee();
  }

  function abort(){
      if(msg.sender == settlor) settlorApprove = false;
      else if (msg.sender == court) courtApprove = false;
      if(!settlorApprove && !courtApprove) fee();
      if(!settlorApprove && !courtApprove) refund();
  }

  function payOut(){
    fee();
    if(beneficiary.send(this.balance)) balances[settlor] = 0;
  }

  function deposit(){
      if(msg.sender == settlor) {
	balances[settlor] += msg.value;
	fee();
      }
      else throw;
  }

  function killContract() internal {
      selfdestruct(court);
      //kills contract and returns funds to court
  }

  function refund(){
    if(courtApprove == false && settlorApprove == false) selfdestruct(settlor);
    //send money back to settlor if both parties agree will is void
  }

  function fee(){
      startup.send(this.balance / 100); //1% fee
  }

}
