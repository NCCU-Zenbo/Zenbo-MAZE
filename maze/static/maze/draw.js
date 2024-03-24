let maze;

async function fetchJsonFileData() {
    let currentUrl = window.location.href;
    let jsonFileUrl = '/get-maze/';

    // // Fetch the JSON file
    // fetch(jsonFileUrl)
    // .then(response => {
    //     if (!response.ok) {
    //         throw new Error('Network response was not ok');
    //     }
    //     return response.json();
    // })
    // .then(data => {
    //     maze = data
    //     console.log(data); // Output the loaded JSON data
    //     console.log(maze);
    //     // Process the JSON data as needed
    // })
    // .catch(error => {
    //     console.error('There was a problem with the fetch operation:', error);
    // });

    try {
        const response = await fetch(jsonFileUrl);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        maze = data;
        // console.log(data); // Output the loaded JSON data
        // console.log(maze);
        // Process the JSON data as needed
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

function draw() {
    // Ensure maze is populated before proceeding
    if (!maze) {
        console.log('Maze data not yet loaded');
        return;
    }

    const canvas = document.querySelector('#canvas');

    if (!canvas.getContext) {
        return;
    }
    const ctx = canvas.getContext('2d');

    // set line stroke and line width
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 3;
    var len_each = 30;
    var offset_x = 10;
    var offset_y = 10;
    console.log(maze);
    var walls = maze.wall;
    for (wall of walls) {
        var now_r = wall.coordinate[0];
        var now_c = wall.coordinate[1];
        // console.log(now_r, now_c);
        ctx.beginPath();
        // ctx.moveTo(offset_x+now_c*len_each, offset_y+now_r*len_each);
        if (wall.isHorizontal){
            ctx.moveTo(offset_x+now_c*len_each-ctx.lineWidth/2, offset_y+now_r*len_each);
            ctx.lineTo(offset_x+now_c*len_each+len_each+ctx.lineWidth/2, offset_y+now_r*len_each);
        }
        else{
            ctx.moveTo(offset_x+now_c*len_each, offset_y+now_r*len_each-ctx.lineWidth/2);
            ctx.lineTo(offset_x+now_c*len_each, offset_y+now_r*len_each+len_each+ctx.lineWidth/2);
        }
        ctx.stroke();

    }
    // ctx.beginPath();
    // ctx.moveTo(10, 10);
    // ctx.lineTo(30, 10);
    // ctx.stroke();

    
    // ctx.beginPath();
    // ctx.moveTo(10, 10);
    // ctx.lineTo(10, 30);
    // ctx.stroke();

}

// Call the function to fetch JSON file data and then call draw() after it's done
fetchJsonFileData().then(draw);
