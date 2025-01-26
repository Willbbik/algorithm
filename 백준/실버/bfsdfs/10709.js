const input = require('fs')
    .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './data.txt')
    .toString()
    .trim()
    .split('\n');

const [H, W] = input[0].split(" ").map(Number);
let map = new Array(H).fill(-1).map(() => new Array(W).fill(-1))
let minute = 1;

for(let i=0; i<H; i++){
    const row = input[i+1].split('');

    for(let j=0; j<W; j++){
        const isCloud = row[j] === 'c';
        const existsCloud = row.includes('c');
        const afterCloud = map[i][j-1] >= 0;

        if(isCloud) {
            map[i][j] = 0;
            minute = 1;
        }

        //행에 구름이 존재하고, 구름뒤에 존재하는 경우에만 카운트
        if(!isCloud && existsCloud && afterCloud) {
            map[i][j] = minute;
            minute++;
        }
    }
}

for(let i=0; i<map.length; i++){
    console.log(map[i].join(" "))
}
