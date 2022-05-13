<template>
    <section class="authors" id="authors">
        <h2>Autorzy</h2>
        <div class="authors__content">
            <box>
                <div class="author">
                    <span class="author__title">Backend</span>
                    <span class="author__name"><a href="https://github.com/filipzygmuntowicz">@filipzygmuntowicz</a></span>
                </div>
                <div class="author">
                    <span class="author__title">Frontend</span>
                    <span class="author__name"><a href="https://github.com/gitfoxcode">@gitFoxCode</a></span>
                </div>
            </box>
        </div>
    </section>
</template>

<style lang="scss" scoped>
.bold{
    font-weight: 900;
}
p{
    font-size: 5rem;
    text-align: center;
    color: #CCC;
    font-weight: 900;
    font-family: "Raleway", sans-serif;
    opacity: 0.5;
    margin-top: 5rem;
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
.authors{
    padding: 0 15%;
    padding-top: 5rem;
    min-height: 50vh;
    position: relative;
    z-index: 1;
    padding-bottom: 5rem;
    background-color: rgb(19,21,60, 0.9);
    background: linear-gradient(0deg, rgba(19,21,60,1) 0%, rgba(19,21,60,1) 50%, rgba(19,21,60,0.8) 100%);
}
.author{
    display: flex;
    flex-direction: column;
    text-align: left;
    color: #FFF;
    gap: 1rem;
}
.box{
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-top: 2rem;
    text-align: center;
}
.author__title{
    font-weight: bold;
    text-transform: uppercase;
}
.author__name a{
    color: #fff;
}
@media (min-width: 850px) {
    .box{
        width: 100%;
        flex-direction: row;
        justify-content: space-evenly;
    }
}
</style>