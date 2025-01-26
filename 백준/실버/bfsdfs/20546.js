const input = require('fs')
    .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './data.txt')
    .toString()
    .split('\n');


const money = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);
const result = junCalculate(money, arr);
const result2 = seongCalculate(money, arr);

if (result > result2) {
    console.log("BNP");
} else if (result < result2) {
    console.log("TIMING");
} else {
    console.log("SAMESAME");
}

function junCalculate(money, arr) {
    let stockNum = 0;
    let lastStockPrice = arr[arr.length - 1];

    for(let i=0; i<arr.length; i++) {

        //현금이 주가보다 많거나 같으면
        if(money >= arr[i]) {
            stockNum += Math.floor(money / arr[i]); //주식 수 상승
            money = money % arr[i];     //현금 차감
        }
    }

    return money + lastStockPrice * stockNum;
}

function seongCalculate(money, arr) {
    let stockNum = 0;
    let lastStockPrice = arr[arr.length - 1];
    let ascDesc = 0;
    let descCount = 0;

    for(let i=1; i<arr.length; i++) {
        
        //가격이 같다면 
        if(arr[i-1] == arr[i]) {
            continue;
        }

        //주가 상승
        if(arr[i-1] < arr[i]) {
            ascDesc++;
            descCount=0;
        }

        //주가 하락
        if(arr[i-1] > arr[i]) {
            descCount++;
            ascDesc=0;
        }

        //매도(판매)
        if(ascDesc >= 3) {
            money += stockNum * arr[i];
            stockNum = 0;
        }

        //매수(구매)
        if(descCount >= 3) {
            if(money >= arr[i]){
                stockNum += Math.floor(money / arr[i]);
                money = money % arr[i];
            }
        }
    }

    return money + lastStockPrice * stockNum;
}