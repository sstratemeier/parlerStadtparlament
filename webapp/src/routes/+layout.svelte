<script>
	import Header from './Header.svelte';
	import './styles.css';
	import Icon from '@iconify/svelte';
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

	<footer>
		<a id="chatbotButton" href="https://chat.openai.com/g/g-ItEJvya2h-parlerstadtparlament" class="fixed bottom-12 right-12  flex align-middle gap-x-2 items-center  text-white rounded-full shadow-lg p-4 bg-white/10  text-sm font-semibold  hover:bg-white/20">
			Chat <Icon class="w-8 h-8 rounded-full"  icon="material-symbols:chat" />
		</a>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
