<script>
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    export let index;
    let left = 20;
    let top = 20;
    let inMotion = false;

    function handleMouseDown() {
        inMotion = true;
    }

    function handleMouseMove(e) {
        if (inMotion) {
            left += e.movementX;
            top += e.movementY;
        }
    }

    function handleMouseUp() {
        inMotion = false;
    }

    function deleteNote() {
        dispatch("remove", { index });
    }
</script>

<div
    on:mousedown={handleMouseDown}
    style="left: {left + index * 5}px; top: {top + index * 5}px;"
    class="note"
>
    <button class="close" on:click={deleteNote}>&times;</button>
    <slot name="text" />
</div>

<svelte:window on:mouseup={handleMouseUp} on:mousemove={handleMouseMove} />

<style>
    .note {
        user-select: none;
        cursor: move;
        border: solid 1px rgb(101, 54, 54);
        position: absolute;
        padding: 20px 30px;
        background-color: rgb(217, 128, 255);
        width: 125px;
        min-height: 125px;
    }

    .close {
        font-weight: 600;
        cursor: pointer;
        position: absolute;
        top: 3%;
        right: 3%;
        padding: 3px;
        color: black;
        background-color: rgb(255, 128, 130);
        border: none;
    }
</style>
