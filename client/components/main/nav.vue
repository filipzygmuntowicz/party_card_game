<template>
    <nav>
        <ul>
            <li><a href="#start" class="active">Start</a></li>
            <li><a href="#rules">Zasady gry</a></li>
            <li><a href="#authors">Autorzy</a></li>
        </ul>
    </nav>
</template>

<script setup>
if (process.client) {
    const sections = [
    ...document.querySelectorAll("section"),
  ];
  let position = window.pageYOffset;
  console.log(position)
  const scrollActive = () => {
    position = window.pageYOffset + 500;
    sections.forEach((section) => {
      if (
        position >= section.offsetTop &&
        position < section.offsetTop + section.offsetHeight
      ) {
        document
          .querySelector(`nav a[href="#${section.id}"]`)
          .classList.add("active");
      } else {
        document
          .querySelector(`nav a[href="#${section.id}"]`)
          .classList.remove("active");
      }
    });
  };
  scrollActive();
  document.addEventListener("scroll", scrollActive);
}
</script>

<style lang="scss" scoped>
nav{
    position: fixed;
    top: 40%;
    right: 10%;
    font-size: 18px;
    text-align: right;
    z-index: 999;
}
ul{
    display: flex;
    flex-direction: column;
    gap: 1em;
}
a{
    text-decoration: none;
    color: #FFF;
    text-transform: uppercase;
    font-family: "Raleway";
    font-weight: 500;
    position: relative;
    transition: all 0.4s;
    &.active{
        font-size: 1.2em;
        font-weight: 900;
        &::after{
            content: "";
            position: absolute;
            top: 50%;
            right: -2.5rem;
            width: 20px;
            height: 20px;
            background-color: #EEE;
            border: 2px solid #FFF;
            border-radius: 50%;
            transform: translateY(-50%)
        }
    }
    &::after{
        content: "";
        position: absolute;
        top: 50%;
        right: -2rem;
        width: 15px;
        height: 15px;
        border: 2px solid #FFF;
        border-radius: 50%;
        transform: translateY(-50%)
    }
}
</style>