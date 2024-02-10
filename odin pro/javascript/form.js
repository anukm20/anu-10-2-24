function frm(e)
{
    e.preventDefault();

    let uname=document.getElementById('uname').value;
    let email=document.getElementById('email').value;
    let pswd=document.getElementById('pswd').value;
    let cpswd=document.getElementById('cpswd').value;
    console.log(uname,email,pswd,cpswd)
    if(pswd==cpswd)
    {
        if(!(uname&&email&&pswd&&cpswd))
        {
            alert('fields are empty')
        }
        else{
           alert('successfully loged in')
        }
    }
    else{
        alert('password not match')
    }
    
}