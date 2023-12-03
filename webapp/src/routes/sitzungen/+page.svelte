<script>
	import Icon from '@iconify/svelte';
	import InfoModal from '../InfoModal.svelte';
  
	let showModal = false;
	
	function toggleModal() {
	  showModal = !showModal;
	}
</script>
  
<div class=" text-white p-4">
	<!-- Main Grid Container -->
	<div class="container mx-auto grid grid-cols-1 md:grid-cols-12 gap-4 md:custom-height-md">
		<!-- Main Content Area -->
		<div class="md:col-span-8 flex flex-col">
			<!-- Neueste Sitzung Section -->
			<a class="text-zinc-100 hover:text-blue-200 hover:no-underline" href="/">
			<div class="bg-neutral-600 p-6 px-8 rounded-3xl mb-4 flex-grow overflow-auto">
				<!-- Content goes here -->
				<h2 class="font-bold text-zinc-100 underline text-2xl mb-2">Neueste Sitzung</h2>
				<p>Samstag, 23.12.2023</p>
				<h2 class="text-2xl">
					"Untersuchung der Haftbedingungen und Überstellungspraktiken im Ausschaffungsgefängnis
					Bazenheid"
				</h2>
				<!-- ... Other content -->
			</div>
		</a>

			<!-- Themen dieses Jahr Section -->
			<div class="bg-neutral-600 p-6 px-8 rounded-3xl flex-grow overflow-auto">
				<!-- Content goes here -->
				<div class="flex justify-between">
					<p>Statistik der Woche</p>
					<button type="button" on:click={toggleModal} class="inline-flex items-center rounded-md bg-white/10 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-white/20">
						Info <Icon class="ml-1 h-8 w-8" icon="material-symbols:info" />
					</button>
					<InfoModal isOpen={showModal} close={() => showModal = false}>
					<!-- Your modal content here -->
					</InfoModal>
				</div>
				<h2 class="font-bold text-zinc-100 underline text-xl mb-2">Eingaben pro Partei pro Jahr</h2>
				<img src="chart01.png" alt="">
				<!-- Add your stats bars or other content here -->
				<!-- ... Other content -->
			</div>
		</div>

		<!-- Sidebar Area -->
		<div class="md:col-span-4 flex flex-col">
			<!-- Sitzungsthemen Section -->
			<div class="bg-neutral-600 p-6 px-8 rounded-3xl flex flex-col h-full mb-4">
				<!-- Content goes here -->
				<h2 class="font-bold text-zinc-100 underline text-2xl mb-2 pb-2">Sitzungsthemen</h2>

				<!-- Buttons container -->
				<div class="flex flex-col flex-grow space-y-2">
					<!-- Each main button with a nested right-aligned "Thema" button -->
					<div
						class="flex justify-between items-center bg-gray-700 text-white rounded-2xl hover:bg-gray-600 text-sm p-2 flex-grow overflow-hidden"
					>
						<span class="truncate">Lorem ipsum dolor sit amet, consectetur adipiscing elit</span>
						<button class="text-white bg-blue-500 hover:bg-blue-400 rounded p-1">Thema</button>
					</div>
					<div
						class="flex justify-between items-center bg-gray-700 text-white rounded-2xl hover:bg-gray-600 text-sm p-2 flex-grow overflow-hidden"
					>
						<span class="truncate"
							>Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</span
						>
						<button class="text-white bg-green-500 hover:bg-green-400 rounded p-1">Thema</button>
					</div>
					<div
						class="flex justify-between items-center bg-gray-700 text-white rounded-2xl hover:bg-gray-600 text-sm p-2 flex-grow overflow-hidden"
					>
						<span class="truncate">Ut enim ad minim veniam, quis nostrud exercitation ullamco</span>
						<button class="text-white bg-red-500 hover:bg-red-400 rounded p-1">Thema</button>
					</div>
					<div
						class="flex justify-between items-center bg-gray-700 text-white rounded-2xl hover:bg-gray-600 text-sm p-2 flex-grow overflow-hidden"
					>
						<span class="truncate">Duis aute irure dolor in reprehenderit in voluptate velit</span>
						<button class="text-white bg-yellow-500 hover:bg-yellow-400 rounded p-1">Thema</button>
					</div>
					<div
						class="flex justify-between items-center bg-gray-700 text-white rounded-2xl hover:bg-gray-600 text-sm p-2 flex-grow overflow-hidden"
					>
						<span class="truncate"
							>Excepteur sint occaecat cupidatat non proident, sunt in culpa</span
						>
						<button class="text-white bg-purple-500 hover:bg-purple-400 rounded p-1">Thema</button>
					</div>
				</div>
			</div>

			<div class="bg-neutral-600 p-6 px-8 rounded-3xl shadow-md">
				<!-- Parteien Section Header -->
				<div class="flex justify-between items-center mb-4">
					<h2 class=" font-bold text-zinc-100 underline text-2xl">Parteien</h2>
					<div class="flex items-center">
						<span class="truncate text-sm text-white mr-2">Eingaben:</span>
						<span class="truncate text-sm text-white">Hauptthemen:</span>
					</div>
				</div>

				<!-- Parteien List -->
				<div class="space-y-2">
					<!-- Party Item -->
					<div class="flex justify-between items-center">
						<a
							href="/gruene"
							class="text-sm font-bold text-white bg-green-700 rounded py-1 text-center w-20 block text-center"
							>Grüne</a
						>
						<span class="text-sm font-bold text-green-500 mx-2">+11%</span>
						<button class="text-white bg-gray-600 hover:bg-gray-500 rounded py-1 truncate px-4"
							>Asyl Politik</button
						>
					</div>
					<!-- Repeat for each party -->
					<div class="flex justify-between items-center">
						<a
							href="/sp"
							class="text-sm font-bold text-white bg-red-700 rounded py-1 text-center w-20 block text-center"
							>SP</a
						>
						<span class="text-sm font-bold text-green-500 mx-2">+8%</span>
						<button class="text-white bg-gray-600 hover:bg-gray-500 rounded py-1 truncate px-4"
							>Asyl Politik</button
						>
					</div>
					<div class="flex justify-between items-center">
						<a
							href="/fdp"
							class="text-sm font-bold text-white bg-blue-700 rounded py-1 text-center w-20 block text-center"
							>FDP</a
						>
						<span class="text-sm font-bold text-green-500 mx-2">+4%</span>
						<button class="text-white bg-gray-600 hover:bg-gray-500 rounded py-1 truncate px-4"
							>Asyl Politik</button
						>
					</div>
					<div class="flex justify-between items-center">
						<a
							href="/svp"
							class="text-sm font-bold text-white bg-green-500 rounded py-1 text-center w-20 block text-center"
							>SVP</a
						>
						<span class="text-sm font-bold text-red-500 mx-2">-8%</span>
						<button class="text-white bg-gray-600 hover:bg-gray-500 rounded py-1 truncate px-4"
							>Asyl Politik</button
						>
					</div>
					<div class="flex justify-between items-center">
						<a
							href="/cvp"
							class="text-sm font-bold text-white bg-orange-700 rounded py-1 text-center w-20 block text-center"
							>CVP</a
						>
						<span class="text-sm font-bold text-red-500 mx-2">-10%</span>
						<button class="text-white bg-gray-600 hover:bg-gray-500 rounded py-1 truncate px-4"
							>Asyl Politik</button
						>
					</div>
				</div>
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
