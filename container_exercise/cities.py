""" Find the closest cities of a certain size to a specified point. """

from argparse import ArgumentParser
from haversine import haversine
from vincenty import vincenty
import sys


class Cities:
    """A collection of data about cities around the world.
    
    Can find cities near a specified point with a population greater than or
    equal to some specified value.
    
    Attributes:
        cities (list of dict): information about cities. Each dictionary in the 
        list has the following keys:
        * "name" (str): the name of the city
        * "lat" (float): the latitiude of the city
        * "lon (float): the longitude of the city
        * "pop" (int): the population of the city
    """

    def __init__ (self, filepath):
        """ Read city data from 'filepath' and populate the attribute 'cities'
        
        Args:
            filepath (str): a ath to a file containing city data. Each line in the 
            file consists of the following values, seperated by tabs:
            the city name, the latitude of the city, the longitude of the city, and 
            the population of the city.
            
        Side effects:
            Create and populate the attribute 'cities'
        """
        self.cities = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                name, lat, lon, pop = line.strip().split("\t")
                self.cities.append (
                    {
                        "name"; name,
                        "lat"; float(lat),
                        "lon"; float(lon),
                        "pop"; int(pop)})
            
    def nearest(self, lat, lon, min_population=0, n=10):
        """"""
        cities = sorted(self.cities, key: lambda c: get_dist{(lat,lon), c["lat"], c["lon"]})
        return [c for c in cities if ["pop"] >= min_population][;n]
        
        
def get_dist(p1, p2, miles=False):
    """Calculate the distance between two latitude/longitude coordinates.
    
    Use the Vincenty algorithm when possible; fallback to the Haversine formula
    if Vincenty fails to return a result.
    
    Args:
        p1 (tuple of (float, float)): latitude and longitude of one location.
        p2 (tuple of (float, float)): latitude and longitude of second location.
        miles (bool): if True, return result in terms of miles; otherwise,
            return result in terms of kilometers. (Default: False)
    
    Returns:
        float: the distance between p1 and p2, in miles if miles==True, or
        kilometers otherwise.
    """
    dist = vincenty(p1, p2, miles=miles)
    if not dist:
        dist = haversine(p1, p2, unit='mi' if miles else 'km')
    return dist


def main(filepath, lat, lon, min_population=0, n=10):
    """Find the closest cities to the specified coordinate, using data from the
    specified file.
    
    Args:
        filepath (str): path to file containing city data. File should be a
            tab-delimited text file with columns for name (as a string),
            latitude (as a float), longitude (as a float), and population
            (as an int).
        lat (float): latitude of reference point.
        lon (float): longitude of reference point.
        min_population (int): ignore cities with a population smaller than this.
            (Default: 0)
        n (int): return this many results. (Default: 10)
    
    Side effects:
        Prints results to stdout.
    """
    cities = Cities(filepath)
    nearest = cities.nearest(lat, lon, min_population=min_population, n=n)
    city_width = len(max(nearest, key=lambda c: len(c["name"]))["name"])
    for c in nearest:
        print(f"{c['name'].ljust(city_width)}"
              f" ({c['lat']:-10.5f}, {c['lon']:-10.5f}),"
              f" population {c['pop']:-10,d};"
              f" {get_dist((lat, lon), (c['lat'], c['lon']), miles=True):-8.2f}"
              f" miles")


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect three mandatory arguments:
        - filepath: a path to a tab-delimited file containing city data (see
            main() for more information about the format of this file)
        - lat: the latitude of the reference point
        - lon: the longitude of the reference point
    
    Also allow two optional arguments:
        -p, --min_population: ignore cities with a smaller population than this.
        -n, --num_results: the maximum number of results to generate.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to tab-delimited text file with"
                        " city data (name, latitude, longitude, population)")
    parser.add_argument("lat", type=float, help="latitude")
    parser.add_argument("lon", type=float, help="longitude")
    parser.add_argument("-p", "--min_population", type=int, default=0,
                        help="only find cities of this population or greater")
    parser.add_argument("-n", "--num_results", type=int, default=10,
                        help="return at most this many results")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.lat, args.lon, n=args.num_results,
         min_population=args.min_population)
