<template>
    <section class="authors" id="authors">
        <h2>Autorzy</h2>
        <div class="authors__content">
            <p>W TRAKCIE...</p>
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
    min-height: 70vh;
    position: relative;
    z-index: 1;
    padding-bottom: 5rem;
    background-color: rgb(19,21,60, 0.9);
    background: linear-gradient(0deg, rgba(19,21,60,1) 0%, rgba(19,21,60,1) 50%, rgba(19,21,60,0.8) 100%);
}

</style>