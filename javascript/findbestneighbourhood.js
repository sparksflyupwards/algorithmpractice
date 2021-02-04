const { SSL_OP_SSLEAY_080_CLIENT_DH_BUG } = require("constants");

let neighbourHoods = [
    {"park": false,
     "gym": false,
    "grocer": false},
    {"park": false,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": false,
   "grocer": false}
]

const requirements = ["gym", "park", "grocer"];



findBestNeighbourhood = (neighbourhoods, requirements)=> { 
    let lowestDistance = {distance: null, index: null};
    let distances = [];
    for(let i=0; i<neighbourHoods.length; i++){
        let max_distance_at_location=-1;
       
            console.log("goig left at "+i)
        for(let req=0; req<requirements.length; req++){
              if(i>0){
                    //traverse left
                for(let left = i-1; left>=0; left-- ){
                    let current_requirement = requirements[req];
                    if(neighbourHoods[left][current_requirement]==true){
                        if((i-left)>max_distance_at_location){
                            max_distance_at_location = i-left;
                        }
                    }
                }
            }
            if(i<requirements.length-1){
                //traverse right
                for(let right = i+1; right<requirements.length; right++){
                    let current_requirement = requirements[req];
                    console.log(neighbourHoods[right] + current_requirement)
                    if(neighbourHoods[right][current_requirement]==true){
                        if((right-i)>max_distance_at_location){
                            max_distance_at_location = right-i;
                        }
                    }
                }
                }
            }
            if(lowestDistance.distance == null || lowestDistance.distance == -1 || lowestDistance.distance > max_distance_at_location){
                lowestDistance.distance = max_distance_at_location;
                lowestDistance.index = i;
            }
            distances.push({distance:max_distance_at_location, index:i})

        }   
        return lowestDistance;
    
}

lowest = findBestNeighbourhood(neighbourHoods, requirements);
console.log(lowest)