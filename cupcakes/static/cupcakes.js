const URL = "http://localhost:5000/api";

function generateHTML(cupcake) {
    return `<div>
                <li id="${cupcake.id}">${cupcake.flavor}, ${cupcake.size}, ${cupcake.rating}
                <button class="delete">X</button></li>
                <img src="${cupcake.image}"></img>
            </div>`;
}

async function displaycupcakes() {
    const response = await axios.get(`${URL}/cupcakes`);

    for (let item of response.data.cupcakes) {
        newcupcake = $(generateHTML(item));
        $("#list-cupcakes").append(newcupcake);
    }
}

$("#cupcakeform").on("submit", async function(evt) {
    evt.preventDefault();

    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();

    const newresponse = await axios.post(`${URL}/cupcakes`);
    let newcake = $(generateHTML(newresponse.data.cupcakes));
    $("#list-cupcakes").append(newcake);
    
});

$("#list-cupcakes").on("click",".delete", async function(evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("li");
    let cupcakeid = $cupcake.attr("id");

    await axios.delete(`${URL}/cupcakes/${cupcakeid}`);
    $cupcake.remove();
})

$(displaycupcakes);