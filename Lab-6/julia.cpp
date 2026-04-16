#include <iostream>
#include <fstream>
#include <cmath>
#include <complex>
#include <cstring>
#include <string>

// Calculates the recursive function z = z^2 + c
double calcz(std::complex<double> z, std::complex<double> c, double zabsmax) {
    int nit = 0;
    int nitmax = 1000;
    double ratio = 0.0; 
    
    while (std::abs(z) < zabsmax && nit < nitmax) {
        z = z * z + c; 
        nit += 1;
        ratio = (double(nit) / nitmax) * 255.0;
    }
    return ratio;
}    
        
void julia_loop(double ***julia, long im_width, long im_height, double xwidth, double yheight, double xmin, double ymin, long nitmax) {
    std::cout << "Calculate the 2D plane..." << std::endl;
    double zabsmax = 10.0;
    std::complex<double> c(-0.1, 0.65);

    // Allocate memory using new to get im_width pointers to an array of doubles
    (*julia) = new double*[im_width];
    
    // Assign each column 
    for (long i = 0; i < im_width; i++) {
        (*julia)[i] = new double[im_height];
    }
  
    // Walk through every pixel and apply calcz()
    for (long ix = 0; ix < im_width; ix++) {
        for (long iy = 0; iy < im_height; iy++) {
            // Map pixel position to a point in the complex plane
            std::complex<double> z( (double(ix) / im_width * xwidth + xmin), 
                                    (double(iy) / im_height * yheight + ymin) );
            
            // Do the iterations
            (*julia)[ix][iy] = calcz(z, c, zabsmax);
        }
    }
}
    
int main(int argc, char **argv) {
    std::string filename = "juliadata.txt";
    if (argc > 1) {
        filename = argv[1];
    }

    std::cout << "Julia set fractal generator\n" << std::endl;

    // Define the variables
    long im_width = 1000;
    long im_height = 1000;
    double xmin = -0.5, xmax = 0.5;
    double xwidth = xmax - xmin;
    double ymin = -0.5, ymax = 0.5;
    double yheight = ymax - ymin;
    long nitmax = 1000;
    double zabsmax = 10.0;

    double **julia; // Pointer to point to the 2D array

    // Call the function over all pixels
    julia_loop(&julia, im_width, im_height, xwidth, yheight, xmin, ymin, nitmax);

    // Write out julia to a txt
    std::ofstream f(filename);
    if (f.is_open()) {
        f << im_width << "\n";
        f << im_height << "\n";
        f << xmin << "\n";
        f << xmax << "\n";
        f << xwidth << "\n";
        f << ymin << "\n";
        f << ymax << "\n";
        f << yheight << "\n";
        
        for (long ix = 0; ix < im_width; ix++) {
            for (long iy = 0; iy < im_height; iy++) {
                f << julia[ix][iy] << "\t";
            }
        }
        f << "\n";
        f.close();
    } else {
        std::cerr << "Error: Could not open file for writing." << std::endl;
        return 1;
    }

    // Clean up dynamically allocated memory
    for (long i = 0; i < im_width; i++) {
        delete[] julia[i];
    }
    delete[] julia;

    return 0;
}