const sections = document.querySelectorAll('section'); //blogs projects...
const nav_list = document.querySelectorAll('nav .w3-bar-block a'); //the blocks in nav

window.addEventListener('scroll', ()=>{
    let current = '';

    sections.forEach( section => {
        const section_top = section.offsetTop;
        const section_height = section.clientHeight;
        if(pageYOffset >= section_top){
            current = section.getAttribute('id');
        }
    })

    nav_list.forEach( a => {
        a.classList.remove('w3-text-teal');
        if(a.classList.contains(current)){
            a.classList.add('w3-text-teal')
        }
    })
})
