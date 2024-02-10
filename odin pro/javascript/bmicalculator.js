function bmi(){
    let a=parseFloat(document.getElementById('wgt').value)
    let b=parseFloat(document.getElementById('hgt').value)
    c=b/100
    d=a/(c**2)
    if(d<18.5){
        a="underweight"
    }
    else if(d>18.5){
        a="normal"
    }
    else if(d>=25){
        a="over weight"
    }
    else{
        a="error"
    }
    let x=document.getElementById('answer')
    x.innerText=d+a
}