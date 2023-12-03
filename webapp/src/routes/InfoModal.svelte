<!-- Modal.svelte -->
<script>
	export let isOpen = false;
	export let close;

	// Function to close the modal
	function closeModal() {
		if (close) close();
	}
</script>

{#if isOpen}
	<div class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">
		<!--
      Background backdrop, show/hide based on modal state.
  
      Entering: "ease-out duration-300"
        From: "opacity-0"
        To: "opacity-100"
      Leaving: "ease-in duration-200"
        From: "opacity-100"
        To: "opacity-0"
    -->
		<div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

		<div class="fixed inset-0 z-10 w-screen overflow-y-auto">
			<div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
				<!--
          Modal panel, show/hide based on modal state.
  
          Entering: "ease-out duration-300"
            From: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            To: "opacity-100 translate-y-0 sm:scale-100"
          Leaving: "ease-in duration-200"
            From: "opacity-100 translate-y-0 sm:scale-100"
            To: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
        -->
				<div
					class="relative transform overflow-hidden rounded-lg bg-gray-800 px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-sm sm:p-6"
				>
					<div>
						<div class="mt-3 text-center  sm:mt-5">
							<h3 class="text-base font-semibold leading-6 text-white" id="modal-title">
								Warum gibt es diesen Ausreisser in 2009?
							</h3>
							<div class="mt-2">
								<p class="text-sm text-gray-300">
									Genau diese Fragen wollen wir durch die Analyse der Daten stellen. Nach der Antwort suchen wir selbst noch. Wenn du Gründe dafür siehst, dann schicke uns deine Meinung auf <a href="mailto:info@parlement.ch">info@parlement.ch</a>
								</p>
							</div>
						</div>
					</div>
					<div class="mt-5 sm:mt-6">
						<button
                            on:click={closeModal}
							type="button"
							class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
							>Zurück</button
						>
					</div>
				</div>
			</div>
		</div>
	</div>
{/if}
