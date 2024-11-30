//Descrip: The st. johns marina is looking for a solution to all the paper they keep about their members and what they pay. This program brings all of that info into one receipt.
//Author: Ben Legge
//Dates: Nov. 16, Nov. 17, Nov 20, Nov. 28, 

//Constants
const HST_RATE = 0.15
const PROCESS_FEE = 59.99
const CANCEL_RATE = 0.60

const cur2Format = new Intl.NumberFormat("en-CA", {
    style: "currency",
    currency: "CAD",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
  });
   
  const per2Format = new Intl.NumberFormat("en-CA", {
    style: "percent",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
  });
   
  const per0Format = new Intl.NumberFormat("en-CA", {
    style: "percent",
    minimumFractionDigits: "0",
    maximumFractionDigits: "0",
  });
   
  const com2Format = new Intl.NumberFormat("en-CA", {
    style: "decimal",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
  });



//Input
let DATE = prompt("Enter current date(YYYY-MM-DD):  ");
let SiteNum = prompt("Enter site number(1-100):  ");
let MemName = prompt("Enter member name:  ");
let MemAddr = prompt("Enter address:  ");
let MemCity = prompt("Enter city:  ");
let MemProv = prompt("Enter province:  ");
let MemCode = prompt("Enter postal code:  ");
let MemHome = prompt("Enter home phone:  ");
let MemCell = prompt("Enter cell phone:  ");
let MemType = prompt("Enter membersip type(S/E):  ");
let MemAlt = prompt("Enter number of alternate members:  ");
let MemClean = prompt("Opt in for weekly cleaning(Y/N):  ");
let MemSurveil = prompt("Opt in for surveillance(Y/N):  ");
SiteNum = parseInt(SiteNum);
MemAlt = parseInt (MemAlt);


//Calculation
let SiteCost
if (SiteNum % 2){
     SiteCost = 80.00;
} else {
     SiteCost = 120.00;
}

let AltCost = MemAlt * 5.00;
let SiteCharge = SiteCost + AltCost;

let CleanCost
if (MemClean == "Y"){
     CleanCost = 50.00;
} else {
     CleanCost = 0.00;
}

let SurvCost
if (MemSurveil == "Y"){
     SurvCost = 35.00;
} else {
     SurvCost = 0.00;
}

let Extra = CleanCost + SurvCost;
let SubTotal = SiteCharge + Extra;
let Tax = SubTotal * HST_RATE;
let Monthly = SubTotal + Tax;

let Dues
if (MemType == "S"){
     Dues = 75.00;
} else {
     Dues = 150.00;
}

let MonthlyFee = Monthly + Dues;
let YearlyFee = MonthlyFee * 12;
let MonthlyPay = (YearlyFee + PROCESS_FEE) / 12;
let Cancel = SiteCharge * CANCEL_RATE;

//Print, except not printing. Same difference.



