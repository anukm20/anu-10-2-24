function empl(e){
    e.preventDefault()
    let emply=document.getElementById('emply').value;
    let sal=document.getElementById('sal').value;
    let exp=document.getElementById('exp').value;
    let slfl=document.getElementById('slfl').value;
    
    console.log(emply,sal,exp,slfl)
    if(!(emply&&sal&&exp&&slfl)){
        alert('fields are empty')
    }
    else{
        alert('succssfully loged in')
    }
}
