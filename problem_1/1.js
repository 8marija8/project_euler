/*

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

*/

let multiples = [];

for (let i = 1; i < 1000; i++) {
  if (i % 3 == 0 || i % 5 == 0) {
    multiples.push(i)
  }
  
}

let total = 0

function sum(numbers) {
  for (let number of numbers) {
    total += number
  }
  console.log(total)
}


sum(multiples)







