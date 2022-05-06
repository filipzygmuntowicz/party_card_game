<template>
	<div class="container">
		<MainNav />
		<MainHero />
		<MainRules />
		<MainAuthors />
	</div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;900&family=Raleway:wght@700;900&display=swap');
body {
	background: linear-gradient(-45deg, #511e58,  #5E0C46, #0B163A);
	background-size: 800% 800%;
	animation: gradient 20s ease infinite;
	height: 100vh;
}
*,*::after,*::before{
	box-sizing: border-box;
	scroll-behavior: smooth;
}
@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}

</style>