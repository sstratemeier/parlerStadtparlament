<script>
	// import Counter from './Counter.svelte';
	// import Chart from './Chart.svelte';

	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';

	// import tradants from './tradants';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<div class="flex mt-8 space-y-16 flex-col">
		<!-- Main Grid Container -->
		<img src="Dashboard.png" alt="" class="container mx-auto rounded-3xl md:custom-height-md" />

		<img src="Heatmap.png" alt="" class="container mx-auto rounded-3xl md:custom-height-md" />
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
