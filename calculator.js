var firstValue = prompt("Enter first value: ")
var secondValue = prompt("Enter second value: ")
var operator = prompt("Enetr operator '+' '-' '/' or '*' ")

//converting inputs to integers
firstValue = parseInt(firstValue)
secondValue = parseInt(secondValue)


var result
if (operator == '+'){
  result = firstValue + secondValue
  
}else if (operator == '-'){
  result = firstValue - secondValue
  
}else if (operator == '*'){
  result = firstValue * secondValue
  
}else{
  result = firstValue / secondValue
}

console.log(result)
