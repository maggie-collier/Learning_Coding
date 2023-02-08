class HelloWorld {
    public static void main(String[] args) {
        // System.out.println("Hello, World!"); 
        // System.out.println("Hi jarod I lvoe you so much"); 

        // Create a new object of type hello world (which is our class HelloWorld on line 1)
        // This allows us to call any of the functions that are within the brackets of this class definition
        HelloWorld myObj = new HelloWorld();

        // Start the section for our first example method
        System.out.println("Header: not string");
        System.out.println(myObj.notString("abc"));

        System.out.println("Header: fibonacci");
        System.out.println(myObj.fibonacci(5));

        // System.out.println("Header: bunny");
        // System.out.println(myObj.bunnyEars(4));
    }
    // general example
    public String notString(String str) {
        System.out.println("Inside not string");
        return "not " + str;
    }
    // recursion example
    public int bunnyEars(int bunnies) {
        System.out.println("Inside bunny ears: " + bunnies);
        if (bunnies == 0) {
            return 0;
        }
            return 2 + bunnyEars(bunnies - 1);
      }
    public int fibonacci(int n) {
        System.out.println("Inside fib: " + n);
        if (n <= 1) {
            return n;
        }
        // fibonacci(n) = fibonacci(n-1) + fibonacci (n-2);
        return fibonacci(n-1) + fibonacci(n-2);
      }
    


}