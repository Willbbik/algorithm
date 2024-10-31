const input = require('fs')
    .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './data.txt')
    .toString()
    .trim()
    .split('\n');

const [N, M] = input[0].split(' ');
let list = new Array(N);

for (let i = 0; i < N; i++) {
    list[i] = i + 1;
}

for (let a = 1; a <= M; a++) {
    let [i, j] = input[a].split(' ').map(Number);

    let item = list[i - 1];
    list[i - 1] = list[j - 1];
    list[j - 1] = item;
}

console.log(list.join(' '));
