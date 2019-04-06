using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentDiary
{
    class diary
    {

        public diary()
        {
            ratings = = new List<float>();
        }

        //  State(variable, data fields)

        List<float> ratings;

        // Behavior

        public void AddRating(float rating)
        {
            ratings.Add(rating);

        }

        public float GetAverange()
        {
            float sum = 0, avg = 0;

            foreach (var rating in ratings)
            {
                sum = sum + rating;
            }

            avg = sum / ratings.Count;

            return avg;
        }

        public float GiveMaxRatig()
        {
            return ratings.Max();
        }
        public float GiveMinRatig()
        {
            return ratings.Min();
        }
    }
}
