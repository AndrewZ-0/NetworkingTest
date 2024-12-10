

async function sortQuery() {
    const vals = document.getElementById("dataInput").value.split(",").map(Number);
    console.log(vals);

    const ip = document.getElementById("ipInput").value;

    const response = await fetch(`${ip}/sort`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: vals
    });

    const data = await response.json();  
    document.getElementById("sortedList").innerText = data.sorted_vals.join(", "); 
}
