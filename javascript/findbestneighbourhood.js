let neighbourHoods = [
    {"park": false,
     "gym": true,
    "grocer": false},
    {"park": false,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": true,
   "grocer": true},
   {"park": true,
    "gym": false,
   "grocer": false},
   {"park": false,
    "gym": false,
   "grocer": true},
   {"park": true,
    "gym": false,
   "grocer": false}
]

const requirements = ["gym", "park", "grocer"];



findBestNeighbourhood = (neighbourhoods, requirements)=> { 
    console.log(requirements);
}

findBestNeighbourhood(neighbourHoods, requirements);