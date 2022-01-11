let p = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("true")
    },
    1000)
    
})
let count = 0;
let counter = ()=>{
    console.log("Count: "+count)
    count ++;
}
let newPromise = (callback, time)=>{
        return new Promise((resolve, reject)=>{ 
            setTimeout( ()=>{
                resolve(callback)
            }, time)
        });
}

console.log(newPromise(counter, 1000)
.then((data)=>newPromise(counter, 1000))
.then(()=>newPromise(counter, 1000))
.then(()=>newPromise(counter, 1000))
.then(()=>newPromise(counter, 1000))
.then(()=>newPromise(counter, 1000))
)

//console.log(newPromise(()=>console.log("ok"), 1000).then((data)=> console.log("then")))