function dec2bin(dec) {
    return (dec >>> 0).toString(2);
  }

function solution(N) {
    let splittedBinary = []
    // converting decimal into binary format
    let nBinary = dec2bin(N)

    // iterating over binary for splitting into a list obj
    for (let i = 0; i < nBinary.length; i++) {
        splittedBinary.push(nBinary.charAt(i))
    }       
    
    let counts=[]
    let counter=0
    // iterating over list for counting gaps
    for (let i=0; i < splittedBinary.length; i++) {
        // checking if element is 0 and i is the last element
        if (i == (splittedBinary.length-1) && splittedBinary[i] == 0) {
            
            counter += 1
            counts.push(counter)
        }
        // if element zero increase by one
        else if (splittedBinary[i] == 0) {
            
            counter += 1
        }

        // if element one push the counter value to the list and reset counter
        else if (splittedBinary[i] == 1) {
            
            counts.push(counter)
            counter = 0
        }
    }

    return Math.max.apply(Math,counts)
}

console.log(solution(200));