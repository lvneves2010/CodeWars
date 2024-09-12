snail = function(array) {
  // enjoy
  let n = array[0].length;
  let fors = n + (n-1)
  let cycles = 0
  newArr = []
  while(fors > 0) {
  for ( i = cycles; i < n - cycles; i++ ) {
    newArr.push(array[cycles][i]);
  }
  fors = fors -1;
  if(fors > 1) {
    for( a = cycles + 1; a < n - cycles; a++ ){
      newArr.push(array[a][n - (cycles +1)])
    }
    fors = fors - 1;
    for( b = 1; b < n - (cycles * 2); b++ ) {
      newArr.push(array[n - (cycles + 1)][n - (cycles + 1) - b]);
    }
    fors = fors - 1;
  }
  if(fors > 1) {
    for(c = n - cycles; c > 2 + cycles; c--) {
      newArr.push(array[c-2][cycles]);
    }
    fors = fors - 1;
    cycles ++
  }
  }
  return newArr;
}