function Partitioning(array, start, end) {
    let pivot = end; 	 
    let pindex = start;  // index for partitioning
    for (let i = start; i < end; ++i) {
        if (array[i] < array[pivot]) {
            let tmp = array[pindex];
            array[pindex] = array[i];
            array[i] = tmp;
            ++pindex;
        }
    }
    tmp = array[pindex];
    array[pindex] = array[pivot];
    array[pivot] = tmp;
    return pindex;
}
function QuickSort(array, start, end) {
    if (start >= end) {
        return;
    }
    let pivot = Partitioning(array, start, end); 
    QuickSort(array, start, pivot - 1);
    QuickSort(array, pivot + 1, end);
}
function main(){
    let array = [9, 0, 2, 7, -2, 6, 1 ];
    document.write("Original array: " + array);
    QuickSort(array, 0, 6);
    console.log(array);
    document.write("Sorted array: " + array);
}
main();
