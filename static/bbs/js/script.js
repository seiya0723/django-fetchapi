window.addEventListener("load" , function (){

    const submit    = document.querySelector("#submit");
    submit.addEventListener( "click", () => { send(); } );

});
const send  = () => {

    // フォームの要素を取得
    const form      = document.querySelector("#form");

    const body      = new FormData(form);
    const url       = form.getAttribute("action");
    const method    = form.getAttribute("method");

    // fetchを使用してPOSTリクエストを送信
    fetch( url, { method , body } )
    .then( response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then( data => {
        if (!data.error){
            const content_area      = document.querySelector("#content_area");
            content_area.innerHTML  = data.content;
        }
    })
    .catch( error => {
        console.log(error);
    });

}
