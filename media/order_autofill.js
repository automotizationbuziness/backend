addEventListener('load', () => {
    var ind = 0;
    while (true) {
        var element = document.getElementById(`id_orders-${ind}-tour`)
        if (!element) break;
        //console.log(element.value, element.options[element.selectedIndex].text)
        element.addEventListener('change', (e) => {
            console.log(e)
            console.log(e.target.id.match(/\d+/)[0])
            var input = document.getElementById(`id_orders-${e.target.id.match(/\d+/)[0]}-cost`)
            console.log(input)
            input.value = e.target.options[e.target.selectedIndex].text.match(/\d+.\d\d руб/)[0].match(/\d+.\d\d/)[0]
            

            const id = e.target.id.match(/\d+/)[0];
            const people = parseFloat(document.getElementById(`id_orders-${id}-cost`).value)
            const count = parseInt(document.getElementById(`id_orders-${id}-tourist_amount`).value)
            console.log(people, count)

            e.target.parentElement.parentElement.parentElement.querySelector('.field-total_cost').children[0].innerHTML = (count * people).toFixed(2)
            
            var els = document.getElementsByClassName('readonly');
            var el = els[els.length - 1]
            
            var acc = 0
            console.log(document.getElementsByClassName('field-total_cost'))
            Array.from(document.getElementsByClassName('field-total_cost')).map((e) => {
                console.log(e, parseFloat(e.children[0].innerHTML))
                if (isNaN(parseFloat(e.children[0].innerHTML.replace(',', '.')))) return;
                else acc += parseFloat(e.children[0].innerHTML.replace(',', '.'))
            }
        )
            el.innerHTML = acc.toFixed(2)
        })


        var element = document.getElementById(`id_orders-${ind}-cost`)
        if (element.value.length == 0) {
            element.value = '1';
        }
        console.log(element)
        element.addEventListener('change', (e) => {
            const id = e.target.id.match(/\d+/)[0];
            const people = parseFloat(e.target.value)
            const count = parseInt(document.getElementById(`id_orders-${id}-tourist_amount`).value)
            e.target.parentElement.parentElement.querySelector('.field-total_cost').children[0].innerHTML = (count * people).toFixed(2)
            
            var els = document.getElementsByClassName('readonly');
            var el = els[els.length - 1]
            
            var acc = 0
            console.log(document.getElementsByClassName('field-total_cost'))
            Array.from(document.getElementsByClassName('field-total_cost')).map((e) => {
                console.log(e, parseFloat(e.children[0].innerHTML))
                if (isNaN(parseFloat(e.children[0].innerHTML.replace(',', '.')))) return;
                else acc += parseFloat(e.children[0].innerHTML.replace(',', '.'))
            }
        )
            console.log(acc)
            el.innerHTML = acc.toFixed(2)
        })

        var element = document.getElementById(`id_orders-${ind}-tourist_amount`)
        if (element.value.length == 0) {
            element.value = '1';
        }
        element.addEventListener('change', (e) => {
            const id = e.target.id.match(/\d+/)[0]
            const people = parseFloat(document.getElementById(`id_orders-${id}-cost`).value)
            const count = parseInt(e.target.value)
            e.target.parentElement.parentElement.querySelector('.field-total_cost').children[0].innerHTML = (count * people).toFixed(2)
            
            var els = document.getElementsByClassName('readonly');
            var el = els[els.length - 1]
            
            var acc = 0
            console.log(document.getElementsByClassName('field-total_cost'))
            Array.from(document.getElementsByClassName('field-total_cost')).map((e) => {
                console.log(e, parseFloat(e.children[0].innerHTML.replace(',', '.')))
                if (isNaN(parseFloat(e.children[0].innerHTML.replace(',', '.')))) return;
                else acc += parseFloat(e.children[0].innerHTML.replace(',', '.'))
            }
        )
            el.innerHTML = acc.toFixed(2)
        })
        ind++;
    }
    
    $('.form-row.field-total_cost').insertBefore('.submit-row')



})