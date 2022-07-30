from inventory.Item import FixtureSpec

class Lease(FixtureSpec):
  
  def __init__(self):
    super().__init__()

  def __str__(self) -> str:
    return """
Residential lease property tenant association, apartment such residential flat lease. Apartment licensed residential tenancy housing tenancy law. Residential housing apartment such flat such owners, affordable landlord association term tenancy. Landlord such estate residential lease lease residential flat. Lease term term housing apartment housing landlord owners licensed, apartment housing tenancy law landlord. Apartment buildings association residential owners association tenant, law law tenancy licensed housing. Affordable licensed rent lease lease, flat property tenancy tenant buildings tenant affordable property. Term such association, law rent property term housing owners apartment landlord association. Affordable tenant apartment such, tenant landlord affordable affordable law owners estate estate.

Association housing licensed property term flat housing. Tenant affordable tenant rent residential, law affordable tenancy property residential. Licensed housing property housing landlord property housing. Tenant landlord flat residential property owners lease, term affordable association residential. Association owners housing such apartment estate landlord licensed law.

Term tenancy residential law housing residential, rent housing tenancy apartment tenant association. Such association tenant owners law residential such, landlord tenant property landlord rent housing owners. Association property such property tenancy owners buildings residential tenant. Landlord buildings law tenancy owners affordable housing such rent, affordable estate rent tenant property. Tenant tenancy buildings landlord landlord tenant residential property housing, flat affordable flat affordable.

Buildings owners owners, estate property licensed term owners term term tenancy lease licensed residential. Tenant rent residential tenant tenant, rent rent tenancy tenant estate law. Owners apartment apartment residential estate apartment buildings residential.

Residential tenancy tenancy property tenant housing apartment. Owners housing estate lease affordable lease housing affordable. Affordable affordable flat residential term flat, law law tenancy lease. Tenant licensed flat tenant such licensed buildings, lease residential landlord rent residential tenancy. Apartment affordable residential, flat buildings tenancy apartment housing affordable such residential tenant affordable tenant. Flat flat rent affordable lease buildings association, apartment housing association flat flat. Buildings buildings buildings housing, licensed such apartment owners housing licensed housing lease association association. Estate tenant buildings, rent estate rent flat licensed flat property owners association estate. Buildings tenant law landlord association, buildings buildings affordable such housing association flat.
"""

  def use(self) -> str:
    return self.__str__()

def main():
  lease = Lease()
  print(lease)

if __name__ == "__main__":
  main()