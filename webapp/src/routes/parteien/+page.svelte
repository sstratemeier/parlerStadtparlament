<script>
	import Icon from '@iconify/svelte';
	import InfoModal from '../InfoModal.svelte';
	import InfoEingabenParteiModal from '../InfoEingabenParteiModal.svelte';

	let showModal = false;

	function toggleModal() {
		showModal = !showModal;
	}
</script>

<div class=" text-white p-4">
	<!-- Main Grid Container -->
	<div class="container mx-auto grid grid-cols-1 md:grid-cols-12 gap-4 md:custom-height-md">
		<!-- Main Content Area -->
		<div class="md:col-span-12 flex flex-col">
			<!-- Themen dieses Jahr Section -->
			<div class="bg-neutral-600 p-6 px-8 rounded-3xl flex-grow overflow-auto">
				<!-- Content goes here -->
				<div class="flex justify-between">
					<p>Statistik der Woche</p>
					<button type="button" on:click={toggleModal} class="inline-flex items-center rounded-md bg-white/10 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-white/20">
						Info <Icon class="ml-1 h-8 w-8" icon="material-symbols:info" />
					</button>
				</div>
				<InfoEingabenParteiModal isOpen={showModal} close={() => (showModal = false)}>
					<!-- Your modal content here -->
				</InfoEingabenParteiModal>
				<h2 class="font-bold text-zinc-100 underline text-xl mb-2">Eingaben pro Partei</h2>
				<img src="parteienanteil.png" alt="" />
				<!-- Add your stats bars or other content here -->
				<!-- ... Other content -->
			</div>
		</div>
	</div>
</div>

<style>
	@media (min-width: 768px) {
		.custom-height-md {
			height: calc(100vh - 100px); /* Full viewport height minus 100px for medium screens and up */
		}
	}
</style>
