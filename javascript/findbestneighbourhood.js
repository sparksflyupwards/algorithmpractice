const { SSL_OP_SSLEAY_080_CLIENT_DH_BUG } = require("constants");

let neighbourHoods = [
    {"park": true,
     "gym": false,
    "grocer": false},
    {"park": false,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": true,
   "grocer": false},
   {"park": false,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": false,
   "grocer": true}
]

const requirements = ["gym", "park", "grocer"];



findBestNeighbourhood = (neighbourhoods, requirements)=> { 
    let lowestDistance = {distance: null, index: null};
    let distances = [];
    for(let i=0; i<neighbourHoods.length; i++){
        let max_distance_at_location=-1;
       
            console.log("goig left at "+i)
            let all_met = 0;
        for(let req=0; req<requirements.length; req++){
              if(i>0){
                    //traverse left
                for(let left = i-1; left>=0; left-- ){
                    let current_requirement = requirements[req];
                    if(neighbourHoods[left][current_requirement]==true){
                        all_met +=1;
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
                        all_met +=1;
                        if((right-i)>max_distance_at_location){
                            max_distance_at_location = right-i;
                        }
                    }
                }
                }

                if(all_met<requirements.length){
                    max_distance_at_location = -1;
                }
            }
            if(lowestDistance.distance == null || lowestDistance.distance == -1 || lowestDistance.distance > max_distance_at_location){
                lowestDistance.distance = max_distance_at_location;
                lowestDistance.index = i;
            }
            distances.push({distance:max_distance_at_location, index:i})

        }   
        console.log(distances)
        return lowestDistance;
    
}

lowest = findBestNeighbourhood(neighbourHoods, requirements);
console.log(lowest)