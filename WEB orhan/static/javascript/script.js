function buttonClick(elem) {
    let name = elem.value.replace("['", "").replace(/', '/g, "#").replace("']", "").replace(/\:::.*/, "").split("#");
    let company = elem.value.split(":::")[1]
    if (name[0] == "Достижения") {
        document.getElementById('text_one').innerHTML = name[1];
        document.getElementById('block1').innerHTML = name[2];
        document.getElementById('photo_one').src="/static/img/" + company + "/photo_1.png";
        document.getElementById('text_two').innerHTML = name[3];
        document.getElementById('block2').innerHTML = name[4];
        document.getElementById('photo_two').src="/static/img/" + company + "/photo_2.png";
        document.getElementById('text_three').innerHTML = name[5];
        document.getElementById('block3').innerHTML = name[6];
        document.getElementById('photo_three').src="/static/img/" + company + "/photo_3.png";
    };
    if (name[0] == "Разработчики") {
        document.getElementById('text_one').innerHTML = name[1];
        document.getElementById('block1').innerHTML = name[2];
        document.getElementById('photo_one').src="/static/img/" + company + "/photo_4.png";
        document.getElementById('text_two').innerHTML = name[3];
        document.getElementById('block2').innerHTML = name[4];
        document.getElementById('photo_two').src="/static/img/" + company + "/photo_5.png";
        document.getElementById('text_three').innerHTML = name[5];
        document.getElementById('block3').innerHTML = name[6];
        document.getElementById('photo_three').src="/static/img/" + company + "/photo_6.png";
    };
    if (name[0] == "История компании") {
        document.getElementById('text_one').innerHTML = name[1];
        document.getElementById('block1').innerHTML = name[2];
        document.getElementById('photo_one').src="/static/img/" + company + "/photo_7.png";
        document.getElementById('text_two').innerHTML = name[3];
        document.getElementById('block2').innerHTML = name[4];
        document.getElementById('photo_two').src="/static/img/" + company + "/photo_8.png";
        document.getElementById('text_three').innerHTML = name[5];
        document.getElementById('block3').innerHTML = name[6];
        document.getElementById('photo_three').src="/static/img/" + company + "/photo_9.png";
    };
};