function show(v, i)
{
    makeVisible(v);
    makeInvisible(i);
}

function makeVisible(x)
{
    x.forEach(element => {
        document.getElementById(element).parentElement.parentElement.className = "";
        document.getElementById(element).labels[0].parentElement.parentElement.className = "";
    });
}

function makeInvisible(x)
{
    x.forEach(element => {
        document.getElementById(element).parentElement.parentElement.className = "invisible";
        document.getElementById(element).labels[0].parentElement.parentElement.className = "invisible";
        document.getElementById(element).value = "";
    });
}
