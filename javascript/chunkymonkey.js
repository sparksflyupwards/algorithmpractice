function chunkArrayInGroups(arr, size) {
    let chunkymonkey = [];
  
    while(arr.length>size){
      let chunky = [];
      for(let i =0; i<size; i++){
        chunky.push(arr.shift());
      }
      chunkymonkey.push(chunky)
    }
    if(arr.length>0){
       chunkymonkey.push(arr);
    }
     
    console.log(chunkymonkey)
  }
  
  chunkArrayInGroups(["a", "b", "c", "d"], 2);
  