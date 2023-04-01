function buttonClick(elem) {
    var text_block_1 = document.querySelector(".text-block_1");
    var text_block_2 = document.querySelector(".text-block_2");
    var text_block_3 = document.querySelector(".text-block_3");
    let name = elem.value.replace("['", "").replace("', '", "#").replace("', '", "#").replace("', '", "#").replace("']", "").split("#");
    text_block_1.innerHTML = name;
    if (name[0] == "Достижения") {
        text_block_1.innerHTML = name[1];
        text_block_2.innerHTML = name[2];
        text_block_3.innerHTML = name[3];
    }
    if (name[0] == "Разработчики") {
        text_block_1.innerHTML = name[1];
        text_block_2.innerHTML = name[2];
        text_block_3.innerHTML = name[3];
    }
    if (name[0] == "История компании") {
        text_block_1.innerHTML = name[1];
        text_block_2.innerHTML = name[2];
        text_block_3.innerHTML = name[3];
    }
};