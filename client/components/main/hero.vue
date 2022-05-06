<template>
    <section class="hero" id="start">
        <article class="box">
            <h1>
                <img src="@/assets/images/logo.svg" alt="Drinking card game">
                <!-- <span class="title__bold">Drinking</span>
                <span class="title__under">card game</span>  -->
            </h1>
            <div class="box__content">
                <div class="box__aside">
                    <div class="aside">
                        <span class="aside__title">5</span>
                        <span class="aside__description">Kategorii</span>
                    </div>
                    <div class="aside">
                        <span class="aside__title">0</span>
                        <span class="aside__description">Ograniczeń</span>
                    </div>
                </div>
                <div class="box__main">
                    <GameCard />
                    <GameCard question="Co byś zrobił gdyby..." color="random"/>
                    <GameCard />
                </div>
                <div class="box__aside">
                    <div class="aside">
                        <span class="aside__title">10550+</span>
                        <span class="aside__description">Pytań</span>
                    </div>
                    <div class="aside">
                        <span class="aside__title">100%</span>
                        <span class="aside__description">Zabawy</span>
                    </div>
                </div>
            </div>
            <a href="/play" class="btn__submit">Zagraj</a>
        </article>
    </section>
</template>

<style scoped lang="scss">
.hero{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 50 50'%3E%3Cg fill-rule='evenodd'%3E%3Cg fill='%239C92AC' transform='matrix(0.875, 0.485, -0.485, 0.875, 8.042, -4.079)' fill-opacity='0.08'%3E%3Cpath d='M20.832,4.555A1,1,0,0,0,20,3H4a1,1,0,0,0-.832,1.554L11,16.3V20H8v2h8V20H13V16.3L20.832,4.555ZM18.132,5l-2,3H7.868l-2-3Z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    &::after{
        content: "";
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
        background: url('@/assets/images/bubble-1.svg'), url('@/assets/images/bubble-2.svg'), url('@/assets/images/bubble-3.svg');
        background-position: 17% 2%, 60% 10%, 70% 80%;
        background-size: 10%;
        background-repeat: no-repeat;
        z-index: 1;
    }
    &::before{
        content: "";
        position: absolute;
        width: 75px;
        height: 75px;
        left: 75%;
        top: 75%;
        background: url('@/assets/images/bubble-4.svg');
        background-position: 80% 95%;
        background-size: cover;
        background-repeat: no-repeat;
        z-index: 3;
    }
}
.box{
    font-family: "Poppins", sans-serif;
    background: hsl(0deg 0% 100% / 8%);
    backdrop-filter: blur( 15px );
    border-radius: 10px;
    // box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
    // border: 1px solid rgba( 255, 255, 255, 0.18 );
    padding: 2rem 4rem;
    text-align: center;
    position: relative;
    z-index: 2;
}
.box__aside{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 2em;
    width: 250px;
}
.box__content{
    display: flex;
    justify-content: space-around;
    margin-top: 2em;
}
.aside{
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: "Raleway", sans-serif;
    text-transform: uppercase;
    color: #FFFFFF;
}
.aside__title{
    font-size: 3em;
    font-weight: 900;
}
.aside__description{
    font-weight: 900;
    margin-top: 0.5em;
}
h1{
    text-align: center;
    color: #FFFFFF;
    font-family: "Raleway", sans-serif;
    text-transform: uppercase;
}
.title__bold{
    display: block;
    font-size: 2em;
    font-weight: 900;
    letter-spacing: 0.2em;
}
.title__under{
    display: block;
    margin-top: 0.2em;
}
.box__main{
    position: relative;
    margin: 0 1rem;
    .card--empty:first-child{
        position: absolute;
        left: 0;
        top: 0;
        z-index: -1;
        transform: translate(25%, 3%) rotate(15deg)
    }
    .card--empty:last-child{
        position: absolute;
        right: 0;
        top: 0;
        z-index: -1;
        transform: translate(-25%, 3%) rotate(-15deg)
    }
}
.btn__submit{
    display: inline-block;
    margin-top: 5rem;
    padding: 1rem 7rem;
    background: linear-gradient(#188D53, #25DE38);
    font-family: "Raleway", sans-serif;
    text-transform: uppercase;
    text-decoration: none;
    color: #FFF;
    font-weight: 900;
    letter-spacing: 1px;
    border-radius: 15px;
    position: relative;
    z-index: 1;
    font-size: 1.2em;
    transition: transform 0.2s;
    &::after{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        backdrop-filter: blur( 15px );
        border-radius: 15px;
        z-index: -1;
    }
    &:hover{
        transform: scale(0.95);
        transition: transform 0.2s;
        &::after{
            opacity: 0;
        }
    }
}
</style>