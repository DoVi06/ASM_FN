
-- số lượng từng loại vật nuôi

SELECT pet_if.Type, COUNT(*) as SL
FROM pet_if
GROUP BY pet_if.Type

-- số lượng vật nuôi không thuần chủng

select count(*) as SL from pf_breed
right join BreedCode on pf_breed.BreedID=BreedCode.BreedID and Breed2='none'

-- số lượng vật nuôi có tình trạng sức khoẻ tốt

select count(*) as SL from pf_health
right join HealthCode on pf_health.HealthID=HealthCode.HealthID and Health='Healthy'
