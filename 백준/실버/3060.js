const input = require('fs')
    .readFileSync(process.platform === 'linux' ? 0 : './data.txt')
    .toString()
    .split('\n');

const N = input.shift();

for(let i=0; i<N; i++) {
    const food = input.shift();
    let pigs = input.shift().split(" ").map(Number);
    let day = 0;
    let totalFood = 0;

    while(food >= totalFood) {
        day++;

        pigs.forEach((pig) => {
            totalFood += pig;
        });

        if(food < totalFood) {
            break;
        }

        let newPigs = [];
        //좌,우,앞에 있는 돼지들 먹이 합산
        for(let k=0; k<pigs.length; k++) {
            let leftPig = k==0 ? pigs.length-1 : k-1;
            let rightPig = k==pigs.length-1 ? 0 : k+1;
            let frontPig = k>2 ? k-3 : k+3;

            const pigFood = pigs[k] + pigs[leftPig] + pigs[rightPig] + pigs[frontPig];
            newPigs.push(pigFood);
        }

        pigs = newPigs;
        totalFood = 0;
    }

    console.log(day)
}