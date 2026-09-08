class DynamicArray {

    private int[] array;
    private int length;

    public DynamicArray(int capacity) {
        this.array = new int[capacity];
        this.length = 0;
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        this.resize();
        this.set(this.length++, n);
    }

    public int popback() {
        return this.array[--this.length];
    }

    private void resize() {
        if (this.getSize() == this.getCapacity()) {
            int[] newArray = new int[this.getCapacity() * 2];
            for (int i = 0; i < this.getCapacity(); i++) newArray[i] = this.array[i];
            this.array = newArray;
        }
    }

    public int getSize() {
        return this.length;
    }

    public int getCapacity() {
        return this.array.length;
    }
}
