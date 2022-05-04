<template>
    <section class="rules" id="rules">
        <h2>Zasady gry</h2>
        <div class="rules__content">
            <img src="@/assets/images/cards.svg" alt="cards" class="rules__img--1">
            <div class="rules__text">
                <p>Zasady gry są takie, że gracz losuje pytanie i na nie odpowiada. Jeżeli odpowiedź jest poprawna to przesuwa w prawo. Jeżeli niepoprawna to przesuwa w lewo. </p>
                <p><span class="bold">1 - KATEGORIA</span> - kategoria pytania</p>
                <p><span class="bold">2 - PYTANIE</span> - pytanie dla gracza</p>
                <p><span class="bold">3 - GRACZ</span> - nazwa gracza, który ma odpowiedzieć</p>
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped>
.bold{
    font-weight: 900;
}
.rules__content{
    margin-top: 2rem;
    display: flex;
    gap: 2rem;
    p:nth-of-type(2){
        margin-top: 2rem;
    }
}
.rules__img--1{
    width: 20rem;
}
.rules__text{
    color: #FFF;
    font-family: "Poppins", sans-serif;
    line-height: 150%;
    max-width: 60ch;
}
h2{
    font-family: "Raleway", sans-serif;
    font-size: 2em;
    font-weight: 900;
    text-transform: uppercase;
    color: #FFF;
    position: relative;
    padding-left: 3rem;
    &::after{
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 0;
        height: 0;
        border-top: 0.5em solid transparent;
        border-left: 1em solid rgb(255, 255, 255);
        border-bottom: 0.5em solid transparent;
        border-radius: 50%;
    
    }
}
.rules{
    padding: 0 15%;
    padding-top: 5rem;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 50 50'%3E%3Cg fill-rule='evenodd'%3E%3Cg fill='%239C92AC' transform='matrix(0.875, 0.485, -0.485, 0.875, 8.042, -4.079)' fill-opacity='0.08'%3E%3Cpath d='M20.832,4.555A1,1,0,0,0,20,3H4a1,1,0,0,0-.832,1.554L11,16.3V20H8v2h8V20H13V16.3L20.832,4.555ZM18.132,5l-2,3H7.868l-2-3Z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    background-size: 2%;
    min-height: 70vh;
    position: relative;
    z-index: 1;
    padding-bottom: 5rem;
    &::after{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(0deg, rgba(19,21,60,1) 0%, rgba(19,21,60,1) 50%, rgba(19,21,60,0) 100%);
        opacity: 0.8;
        z-index: -1;
    }
}

</style>