const sleep = m => new Promise(r => setTimeout(r, m))


window.addEventListener('load', () => {
    document.getElementById('id_sale').addEventListener('change', (e) => {
        try {
            document.getElementById('id_total_cost').value = e.target.options[e.target.selectedIndex].text.match(/\d+.\d\dруб/)[0].match(/\d+.\d\d/)[0];
        }
        catch {
            document.getElementById('id_total_cost').value = '0.00';
        }        
    })
    // var button = document.evaluate("//input[@value='Сохранить и продолжить редактирование']", document, null, XPathResult.ANY_TYPE, null).iterateNext()
    // console.log(button)
    // button.onclick = async () => {
    //     const res = await fetch('/order/get')
    //     if (res.ok) {
    //         var body = await res.text();
    //         body = parseInt(body) + 1
    //         setTimeout(() => {
    //             window.location.replace(`/admin/toursale/toursaleend/${body}/change/`)
    //         })
    //     }
    // }
})
