<template>
    <div class="box">
        <slot></slot>
    </div>
</template>

<style lang="scss" scoped>
.box{
    display: block;
    width: max-content;
    font-family: "Poppins", sans-serif;
    background: hsl(0deg 0% 100% / 8%);
    backdrop-filter: blur( 15px );
    border-radius: 10px;
    padding: 2rem 4rem;
    text-align: center;
    position: relative;
    z-index: 2;
}
</style>