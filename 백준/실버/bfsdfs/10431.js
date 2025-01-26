const input = require('fs')
    .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './data.txt')
    .toString()
    .trim()
    .split('\n');


const P = input.shift();

for(let i=0; i<P; i++){
    let arr = input[i].split(" ").map(Number);
    const [T, result] = insertionSort(arr);

    console.log(T + " " + result)
}


//삽입 정렬
function insertionSort(arr) {
    let result = 0;
    const T = arr.shift();

    for(let j=1; j<arr.length; j++) {

        //비교하려는 기준 값
        const k = arr[j];

        //기준값 앞에 있는 요소
        let frontIndex=j-1;

        //앞요소가 현재값보다 큰 경우에만
        for(frontIndex; frontIndex>=0 && arr[frontIndex] > k; frontIndex--){
            //앞요소 뒤로 이동시킴
            arr[frontIndex+1] = arr[frontIndex];
            result++;
        }

        //더 이상 앞으로 이동할 수 없는 경우
        //앞으로 계속 이동해온 현재 위치에 비교기준 값 할당
        arr[frontIndex+1] = k
    }

    return [T, result];
}