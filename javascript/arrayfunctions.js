let cars = ["Mercedes","Toyota","Tesla","Audi"];
let plants = ["Apple Tree","Garlic Grass","Tulips"];

let toTen = [1,2,3,4,5,6,7,8,9,10];
let toFive = [1,2,3,4,5]
//concat
console.log("concat cars and plants: "+cars.concat(plants))

//forEach
console.log("print all the even numbers using forEach " +
            toTen.forEach(
                (element) =>{
                    if (element%2==0){
                        console.log(element)
                    }
                }
            ))


//Array from to create array from string object print all constants using the map function
Array.from("this string",
         (elem)=>{
             if(!["a","e","i","o","u"].includes(String(elem))){
                 console.log(elem)
             }})